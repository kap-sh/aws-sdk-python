"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails(TypedDict):
    options: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>The options to use to configure the log router.</p> <p>The valid option keys are as follows:</p> <ul> <li> <p> <code>enable-ecs-log-metadata</code>. The value can be <code>true</code> or <code>false</code>.</p> </li> <li> <p> <code>config-file-type</code>. The value can be <code>s3</code> or <code>file</code>.</p> </li> <li> <p> <code>config-file-value</code>. The value is either an S3 ARN or a file path.</p> </li> </ul>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The log router to use. Valid values are <code>fluentbit</code> or <code>fluentd</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails,
) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_securityhub.types.field_map

        out["Options"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["options"]
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_securityhub.types.field_map

        out["options"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["Options"]
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
