"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BlockchainInstant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class BlockchainInstant(TypedDict, closed=True):
    time: NotRequired["datetime.datetime"]
    """<p>The container of the <code>Timestamp</code> of the blockchain instant.</p> <note> <p>This <code>timestamp</code> will only be recorded up to the second.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockchainInstant) -> dict:
    out: dict = {}
    if "time" in value:
        import aws_sdk_managedblockchain_query.types._prelude.timestamp

        out["time"] = (
            aws_sdk_managedblockchain_query.types._prelude.timestamp.serialize_json(
                value["time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlockchainInstant:
    out: BlockchainInstant = {}  # type: ignore[typeddict-item]
    if "time" in data:
        import aws_sdk_managedblockchain_query.types._prelude.timestamp

        out["time"] = (
            aws_sdk_managedblockchain_query.types._prelude.timestamp.deserialize_json(
                data["time"]
            )
        )
    return out
