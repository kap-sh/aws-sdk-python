"""Generated from Smithy shape ``com.amazonaws.glacier#DescribeVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.long
    import capo_glacier.types.string


class DescribeVaultOutput(TypedDict, closed=True):
    vault_arn: NotRequired["capo_glacier.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the vault.</p>"""
    vault_name: NotRequired["capo_glacier.types.string.string"]
    """<p>The name of the vault.</p>"""
    creation_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example <code>2012-03-20T17:03:43.221Z</code>.</p>"""
    last_inventory_date: NotRequired["capo_glacier.types.string.string"]
    """<p>The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example <code>2012-03-20T17:03:43.221Z</code>.</p>"""
    number_of_archives: "capo_glacier.types.long.long"
    """<p>The number of archives in the vault as of the last inventory date. This field will return <code>null</code> if an inventory has not yet run on the vault, for example if you just created the vault.</p>"""
    size_in_bytes: "capo_glacier.types.long.long"
    """<p>Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVaultOutput) -> dict:
    out: dict = {}
    if "vault_arn" in value:
        out["VaultARN"] = value["vault_arn"]
    if "vault_name" in value:
        out["VaultName"] = value["vault_name"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "last_inventory_date" in value:
        out["LastInventoryDate"] = value["last_inventory_date"]
    out["NumberOfArchives"] = value.get("number_of_archives", 0)
    out["SizeInBytes"] = value.get("size_in_bytes", 0)
    return out


def deserialize_json(data: dict) -> DescribeVaultOutput:
    out: DescribeVaultOutput = {}  # type: ignore[typeddict-item]
    if "VaultARN" in data:
        out["vault_arn"] = data["VaultARN"]
    if "VaultName" in data:
        out["vault_name"] = data["VaultName"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "LastInventoryDate" in data:
        out["last_inventory_date"] = data["LastInventoryDate"]
    if "NumberOfArchives" in data:
        out["number_of_archives"] = data["NumberOfArchives"]
    else:
        out["number_of_archives"] = 0
    if "SizeInBytes" in data:
        out["size_in_bytes"] = data["SizeInBytes"]
    else:
        out["size_in_bytes"] = 0
    return out
