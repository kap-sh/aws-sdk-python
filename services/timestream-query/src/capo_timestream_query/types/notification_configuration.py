"""Generated from Smithy shape ``com.amazonaws.timestreamquery#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.sns_configuration


class NotificationConfiguration(TypedDict, closed=True):
    sns_configuration: "capo_timestream_query.types.sns_configuration.SnsConfiguration"
    """<p>Details about the Amazon Simple Notification Service (SNS) configuration. This field is visible only when SNS Topic is provided when updating the account settings. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotificationConfiguration) -> dict:
    out: dict = {}
    import capo_timestream_query.types.sns_configuration

    out["SnsConfiguration"] = (
        capo_timestream_query.types.sns_configuration.serialize_aws_json_1_0(
            value["sns_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "SnsConfiguration" in data:
        import capo_timestream_query.types.sns_configuration

        out["sns_configuration"] = (
            capo_timestream_query.types.sns_configuration.deserialize_aws_json_1_0(
                data["SnsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationConfiguration.sns_configuration required"
        )
    return out
