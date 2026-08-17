"""Generated from Smithy shape ``com.amazonaws.ecs#IngressPathSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.ingress_path_summary

IngressPathSummaries: TypeAlias = list[
    "capo_ecs.types.ingress_path_summary.IngressPathSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngressPathSummaries) -> list:
    import capo_ecs.types.ingress_path_summary

    out: list = []
    for item in value:
        out.append(capo_ecs.types.ingress_path_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IngressPathSummaries:
    import capo_ecs.types.ingress_path_summary

    out: IngressPathSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.ingress_path_summary.deserialize_aws_json_1_1(item))
    return out
