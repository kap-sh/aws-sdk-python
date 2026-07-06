"""Generated from Smithy shape ``com.amazonaws.mwaa#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_arn
    import aws_sdk_mwaa.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_mwaa.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>"""
    tag_keys: "aws_sdk_mwaa.types.tag_key_list.TagKeyList"
    r"""<p>The key-value tag pair you want to remove. For example, <code>\"Environment\": \"Staging\"</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
