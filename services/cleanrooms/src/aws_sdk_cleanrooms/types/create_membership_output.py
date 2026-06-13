"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateMembershipOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership


class CreateMembershipOutput(TypedDict):
    membership: "aws_sdk_cleanrooms.types.membership.Membership"
    """<p>The membership that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.membership

    out["membership"] = aws_sdk_cleanrooms.types.membership.serialize_json(
        value["membership"]
    )
    return out


def deserialize_json(data: dict) -> CreateMembershipOutput:
    out: CreateMembershipOutput = {}  # type: ignore[typeddict-item]
    if "membership" in data:
        import aws_sdk_cleanrooms.types.membership

        out["membership"] = aws_sdk_cleanrooms.types.membership.deserialize_json(
            data["membership"]
        )
    else:
        raise DeserializationError("CreateMembershipOutput.membership required")
    return out
