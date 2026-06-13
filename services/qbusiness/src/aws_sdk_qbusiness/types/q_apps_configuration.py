"""Generated from Smithy shape ``com.amazonaws.qbusiness#QAppsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.q_apps_control_mode


class QAppsConfiguration(TypedDict):
    q_apps_control_mode: "aws_sdk_qbusiness.types.q_apps_control_mode.QAppsControlMode"
    """<p>Status information about whether end users can create and use Amazon Q Apps in the web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QAppsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.q_apps_control_mode

    out["qAppsControlMode"] = (
        aws_sdk_qbusiness.types.q_apps_control_mode.serialize_json(
            value["q_apps_control_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> QAppsConfiguration:
    out: QAppsConfiguration = {}  # type: ignore[typeddict-item]
    if "qAppsControlMode" in data:
        import aws_sdk_qbusiness.types.q_apps_control_mode

        out["q_apps_control_mode"] = (
            aws_sdk_qbusiness.types.q_apps_control_mode.deserialize_json(
                data["qAppsControlMode"]
            )
        )
    else:
        raise DeserializationError("QAppsConfiguration.q_apps_control_mode required")
    return out
