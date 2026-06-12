"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetAccessorOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor


class GetAccessorOutput(TypedDict):
    accessor: NotRequired["aws_sdk_managedblockchain.types.accessor.Accessor"]
    """<p>The properties of the accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessorOutput) -> dict:
    out: dict = {}
    if "accessor" in value:
        import aws_sdk_managedblockchain.types.accessor

        out["Accessor"] = aws_sdk_managedblockchain.types.accessor.serialize_json(
            value["accessor"]
        )
    return out


def deserialize_json(data: dict) -> GetAccessorOutput:
    out: GetAccessorOutput = {}  # type: ignore[typeddict-item]
    if "Accessor" in data:
        import aws_sdk_managedblockchain.types.accessor

        out["accessor"] = aws_sdk_managedblockchain.types.accessor.deserialize_json(
            data["Accessor"]
        )
    return out
