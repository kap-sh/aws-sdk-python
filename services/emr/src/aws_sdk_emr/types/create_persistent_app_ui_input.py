"""Generated from Smithy shape ``com.amazonaws.emr#CreatePersistentAppUIInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.emr_containers_config
    import aws_sdk_emr.types.profiler_type
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.tag_list


class CreatePersistentAppUIInput(TypedDict):
    target_resource_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The unique Amazon Resource Name (ARN) of the target resource.</p>"""
    emr_containers_config: NotRequired[
        "aws_sdk_emr.types.emr_containers_config.EMRContainersConfig"
    ]
    """<p>The EMR containers configuration.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>Tags for the persistent application user interface.</p>"""
    x_referer: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The cross reference for the persistent application user interface.</p>"""
    profiler_type: NotRequired["aws_sdk_emr.types.profiler_type.ProfilerType"]
    """<p>The profiler type for the persistent application user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePersistentAppUIInput) -> dict:
    out: dict = {}
    if "target_resource_arn" in value:
        out["TargetResourceArn"] = value["target_resource_arn"]
    if "emr_containers_config" in value:
        import aws_sdk_emr.types.emr_containers_config

        out["EMRContainersConfig"] = (
            aws_sdk_emr.types.emr_containers_config.serialize_aws_json_1_1(
                value["emr_containers_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "x_referer" in value:
        out["XReferer"] = value["x_referer"]
    if "profiler_type" in value:
        import aws_sdk_emr.types.profiler_type

        out["ProfilerType"] = aws_sdk_emr.types.profiler_type.serialize_aws_json_1_1(
            value["profiler_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePersistentAppUIInput:
    out: CreatePersistentAppUIInput = {}  # type: ignore[typeddict-item]
    if "TargetResourceArn" in data:
        out["target_resource_arn"] = data["TargetResourceArn"]
    if "EMRContainersConfig" in data:
        import aws_sdk_emr.types.emr_containers_config

        out["emr_containers_config"] = (
            aws_sdk_emr.types.emr_containers_config.deserialize_aws_json_1_1(
                data["EMRContainersConfig"]
            )
        )
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "XReferer" in data:
        out["x_referer"] = data["XReferer"]
    if "ProfilerType" in data:
        import aws_sdk_emr.types.profiler_type

        out["profiler_type"] = aws_sdk_emr.types.profiler_type.deserialize_aws_json_1_1(
            data["ProfilerType"]
        )
    return out
