"""Generated from Smithy shape ``com.amazonaws.kms#DeleteAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_name_type


class DeleteAliasRequest(TypedDict):
    alias_name: "aws_sdk_kms.types.alias_name_type.AliasNameType"
    """<p>The alias to be deleted. The alias name must begin with <code>alias/</code> followed by the alias name, such as <code>alias/ExampleAlias</code>.</p>"""
