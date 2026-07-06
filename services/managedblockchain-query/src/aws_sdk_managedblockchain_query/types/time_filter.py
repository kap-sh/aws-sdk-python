"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TimeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.blockchain_instant

TimeFilter = TypedDict(
    "TimeFilter",
    {
        "from": NotRequired[
            "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ],
        "to": NotRequired[
            "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: TimeFilter) -> dict:
    out: dict = {}
    if "from" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["from"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["from"]
            )
        )
    if "to" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["to"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["to"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeFilter:
    out: TimeFilter = {}  # type: ignore[typeddict-item]
    if "from" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["from"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["from"]
            )
        )
    if "to" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["to"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["to"]
            )
        )
    return out
