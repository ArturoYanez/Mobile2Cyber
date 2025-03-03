return require('packer').startup(function()
    use 'wbthomason/packer.nvim'  -- Gestor de plugins
    use 'nvim-treesitter/nvim-treesitter'  -- Mejor sintaxis
    use 'lewis6991/gitsigns.nvim'  -- Integración con Git
end)
