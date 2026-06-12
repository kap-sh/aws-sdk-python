"""Generated from Smithy shape ``com.amazonaws.sagemaker#VisibilityConditions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.visibility_conditions_key
    import aws_sdk_sagemaker.types.visibility_conditions_value


class VisibilityConditions(TypedDict):
    key: NotRequired[
        "aws_sdk_sagemaker.types.visibility_conditions_key.VisibilityConditionsKey"
    ]
    """<p>The key that specifies the tag that you're using to filter the search results. It must be in the following format: <code>Tags.&lt;key&gt;</code>.</p>"""
    value: NotRequired[
        "aws_sdk_sagemaker.types.visibility_conditions_value.VisibilityConditionsValue"
    ]
    """<p>The value for the tag that you're using to filter the search results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VisibilityConditions) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VisibilityConditions:
    out: VisibilityConditions = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
