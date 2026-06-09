"""Generated from Smithy shape ``com.amazonaws.eks#UpdateAccessConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.authentication_mode


class UpdateAccessConfigRequest(TypedDict):
    authentication_mode: NotRequired[
        "aws_sdk_eks.types.authentication_mode.AuthenticationMode"
    ]
    """<p>The desired authentication mode for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessConfigRequest) -> dict:
    out: dict = {}
    if "authentication_mode" in value:
        import aws_sdk_eks.types.authentication_mode

        out["authenticationMode"] = (
            aws_sdk_eks.types.authentication_mode.serialize_json(
                value["authentication_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccessConfigRequest:
    out: UpdateAccessConfigRequest = {}  # type: ignore[typeddict-item]
    if "authenticationMode" in data:
        import aws_sdk_eks.types.authentication_mode

        out["authentication_mode"] = (
            aws_sdk_eks.types.authentication_mode.deserialize_json(
                data["authenticationMode"]
            )
        )
    return out
