"""Generated from Smithy shape ``com.amazonaws.mwaa#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_arn

class ListTagsForResourceInput(TypedDict):
    resource_arn: "aws_sdk_mwaa.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out