"""Generated from Smithy shape ``com.amazonaws.qbusiness#PersonalizationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.personalization_control_mode


class PersonalizationConfiguration(TypedDict):
    personalization_control_mode: "aws_sdk_qbusiness.types.personalization_control_mode.PersonalizationControlMode"
    """<p>An option to allow Amazon Q Business to customize chat responses using user specific metadata—specifically, location and job information—in your IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersonalizationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.personalization_control_mode

    out["personalizationControlMode"] = (
        aws_sdk_qbusiness.types.personalization_control_mode.serialize_json(
            value["personalization_control_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> PersonalizationConfiguration:
    out: PersonalizationConfiguration = {}  # type: ignore[typeddict-item]
    if "personalizationControlMode" in data:
        import aws_sdk_qbusiness.types.personalization_control_mode

        out["personalization_control_mode"] = (
            aws_sdk_qbusiness.types.personalization_control_mode.deserialize_json(
                data["personalizationControlMode"]
            )
        )
    else:
        raise DeserializationError(
            "PersonalizationConfiguration.personalization_control_mode required"
        )
    return out
