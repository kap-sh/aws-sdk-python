"""Generated from Smithy shape ``com.amazonaws.lightsail#NameServersUpdateState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.name_servers_update_state_code
    import aws_sdk_lightsail.types.string


class NameServersUpdateState(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_lightsail.types.name_servers_update_state_code.NameServersUpdateStateCode"
    ]
    """<p>The status code for the name servers update.</p> <p>Following are the possible values:</p> <ul> <li> <p> <code>SUCCEEDED</code> - The name server records were successfully updated.</p> </li> <li> <p> <code>PENDING</code> - The name server record update is in progress.</p> </li> <li> <p> <code>FAILED</code> - The name server record update failed.</p> </li> <li> <p> <code>STARTED</code> - The automatic name server record update started.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The message that describes the reason for the status code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NameServersUpdateState) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_lightsail.types.name_servers_update_state_code

        out["code"] = (
            aws_sdk_lightsail.types.name_servers_update_state_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NameServersUpdateState:
    out: NameServersUpdateState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_lightsail.types.name_servers_update_state_code

        out["code"] = (
            aws_sdk_lightsail.types.name_servers_update_state_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
