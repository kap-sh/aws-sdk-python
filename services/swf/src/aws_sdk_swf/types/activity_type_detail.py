"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTypeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_type_configuration
    import aws_sdk_swf.types.activity_type_info


class ActivityTypeDetail(TypedDict, closed=True):
    type_info: "aws_sdk_swf.types.activity_type_info.ActivityTypeInfo"
    """<p>General information about the activity type.</p> <p>The status of activity type (returned in the ActivityTypeInfo structure) can be one of the following.</p> <ul> <li> <p> <code>REGISTERED</code> – The type is registered and available. Workers supporting this type should be running. </p> </li> <li> <p> <code>DEPRECATED</code> – The type was deprecated using <a>DeprecateActivityType</a>, but is still in use. You should keep workers supporting this type running. You cannot create new tasks of this type. </p> </li> </ul>"""
    configuration: (
        "aws_sdk_swf.types.activity_type_configuration.ActivityTypeConfiguration"
    )
    """<p>The configuration settings registered with the activity type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTypeDetail) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.activity_type_info

    out["typeInfo"] = aws_sdk_swf.types.activity_type_info.serialize_aws_json_1_0(
        value["type_info"]
    )
    import aws_sdk_swf.types.activity_type_configuration

    out["configuration"] = (
        aws_sdk_swf.types.activity_type_configuration.serialize_aws_json_1_0(
            value["configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTypeDetail:
    out: ActivityTypeDetail = {}  # type: ignore[typeddict-item]
    if "typeInfo" in data:
        import aws_sdk_swf.types.activity_type_info

        out["type_info"] = (
            aws_sdk_swf.types.activity_type_info.deserialize_aws_json_1_0(
                data["typeInfo"]
            )
        )
    else:
        raise DeserializationError("ActivityTypeDetail.type_info required")
    if "configuration" in data:
        import aws_sdk_swf.types.activity_type_configuration

        out["configuration"] = (
            aws_sdk_swf.types.activity_type_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("ActivityTypeDetail.configuration required")
    return out
