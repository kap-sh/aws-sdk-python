"""Generated from Smithy shape ``com.amazonaws.emr#CreatePersistentAppUIInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.emr_containers_config
    import capo_emr.types.profiler_type
    import capo_emr.types.string
    import capo_emr.types.tag_list


class CreatePersistentAppUIInput(TypedDict, closed=True):
    target_resource_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The unique Amazon Resource Name (ARN) of the target resource.</p>"""
    emr_containers_config: NotRequired[
        "capo_emr.types.emr_containers_config.EMRContainersConfig"
    ]
    """<p>The EMR containers configuration.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>Tags for the persistent application user interface.</p>"""
    x_referer: NotRequired["capo_emr.types.string.String"]
    """<p>The cross reference for the persistent application user interface.</p>"""
    profiler_type: NotRequired["capo_emr.types.profiler_type.ProfilerType"]
    """<p>The profiler type for the persistent application user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePersistentAppUIInput) -> dict:
    out: dict = {}
    if "target_resource_arn" in value:
        out["TargetResourceArn"] = value["target_resource_arn"]
    if "emr_containers_config" in value:
        import capo_emr.types.emr_containers_config

        out["EMRContainersConfig"] = (
            capo_emr.types.emr_containers_config.serialize_aws_json_1_1(
                value["emr_containers_config"]
            )
        )
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "x_referer" in value:
        out["XReferer"] = value["x_referer"]
    if "profiler_type" in value:
        import capo_emr.types.profiler_type

        out["ProfilerType"] = capo_emr.types.profiler_type.serialize_aws_json_1_1(
            value["profiler_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePersistentAppUIInput:
    out: CreatePersistentAppUIInput = {}  # type: ignore[typeddict-item]
    if "TargetResourceArn" in data:
        out["target_resource_arn"] = data["TargetResourceArn"]
    if "EMRContainersConfig" in data:
        import capo_emr.types.emr_containers_config

        out["emr_containers_config"] = (
            capo_emr.types.emr_containers_config.deserialize_aws_json_1_1(
                data["EMRContainersConfig"]
            )
        )
    if "Tags" in data:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "XReferer" in data:
        out["x_referer"] = data["XReferer"]
    if "ProfilerType" in data:
        import capo_emr.types.profiler_type

        out["profiler_type"] = capo_emr.types.profiler_type.deserialize_aws_json_1_1(
            data["ProfilerType"]
        )
    return out
