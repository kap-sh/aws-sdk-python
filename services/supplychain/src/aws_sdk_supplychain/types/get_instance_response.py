"""Generated from Smithy shape ``com.amazonaws.supplychain#GetInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.instance


class GetInstanceResponse(TypedDict, closed=True):
    instance: "aws_sdk_supplychain.types.instance.Instance"
    """<p>The instance resource data details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.instance

    out["instance"] = aws_sdk_supplychain.types.instance.serialize_json(
        value["instance"]
    )
    return out


def deserialize_json(data: dict) -> GetInstanceResponse:
    out: GetInstanceResponse = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import aws_sdk_supplychain.types.instance

        out["instance"] = aws_sdk_supplychain.types.instance.deserialize_json(
            data["instance"]
        )
    else:
        raise DeserializationError("GetInstanceResponse.instance required")
    return out
