"""Generated from Smithy shape ``com.amazonaws.glacier#ListVaultsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string
    import aws_sdk_glacier.types.vault_list


class ListVaultsOutput(TypedDict):
    vault_list: NotRequired["aws_sdk_glacier.types.vault_list.VaultList"]
    """<p>List of vaults.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The vault ARN at which to continue pagination of the results. You use the marker in another List Vaults request to obtain more vaults in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVaultsOutput) -> dict:
    out: dict = {}
    if "vault_list" in value:
        import aws_sdk_glacier.types.vault_list

        out["VaultList"] = aws_sdk_glacier.types.vault_list.serialize_json(
            value["vault_list"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> ListVaultsOutput:
    out: ListVaultsOutput = {}  # type: ignore[typeddict-item]
    if "VaultList" in data:
        import aws_sdk_glacier.types.vault_list

        out["vault_list"] = aws_sdk_glacier.types.vault_list.deserialize_json(
            data["VaultList"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
