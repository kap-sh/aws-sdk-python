"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CloudWatchDimensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.default_dimension_value
    import aws_sdk_pinpoint_email.types.dimension_name
    import aws_sdk_pinpoint_email.types.dimension_value_source


class CloudWatchDimensionConfiguration(TypedDict, closed=True):
    dimension_name: "aws_sdk_pinpoint_email.types.dimension_name.DimensionName"
    """<p>The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""
    dimension_value_source: (
        "aws_sdk_pinpoint_email.types.dimension_value_source.DimensionValueSource"
    )
    """<p>The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose <code>messageTag</code>. If you want Amazon Pinpoint to use your own email headers, choose <code>emailHeader</code>. If you want Amazon Pinpoint to use link tags, choose <code>linkTags</code>.</p>"""
    default_dimension_value: (
        "aws_sdk_pinpoint_email.types.default_dimension_value.DefaultDimensionValue"
    )
    """<p>The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDimensionConfiguration) -> dict:
    out: dict = {}
    out["DimensionName"] = value["dimension_name"]
    import aws_sdk_pinpoint_email.types.dimension_value_source

    out["DimensionValueSource"] = (
        aws_sdk_pinpoint_email.types.dimension_value_source.serialize_json(
            value["dimension_value_source"]
        )
    )
    out["DefaultDimensionValue"] = value["default_dimension_value"]
    return out


def deserialize_json(data: dict) -> CloudWatchDimensionConfiguration:
    out: CloudWatchDimensionConfiguration = {}  # type: ignore[typeddict-item]
    if "DimensionName" in data:
        out["dimension_name"] = data["DimensionName"]
    else:
        raise DeserializationError(
            "CloudWatchDimensionConfiguration.dimension_name required"
        )
    if "DimensionValueSource" in data:
        import aws_sdk_pinpoint_email.types.dimension_value_source

        out["dimension_value_source"] = (
            aws_sdk_pinpoint_email.types.dimension_value_source.deserialize_json(
                data["DimensionValueSource"]
            )
        )
    else:
        raise DeserializationError(
            "CloudWatchDimensionConfiguration.dimension_value_source required"
        )
    if "DefaultDimensionValue" in data:
        out["default_dimension_value"] = data["DefaultDimensionValue"]
    else:
        raise DeserializationError(
            "CloudWatchDimensionConfiguration.default_dimension_value required"
        )
    return out
