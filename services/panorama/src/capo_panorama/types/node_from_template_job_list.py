"""Generated from Smithy shape ``com.amazonaws.panorama#NodeFromTemplateJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.node_from_template_job

NodeFromTemplateJobList: TypeAlias = list[
    "capo_panorama.types.node_from_template_job.NodeFromTemplateJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeFromTemplateJobList) -> list:
    import capo_panorama.types.node_from_template_job

    out: list = []
    for item in value:
        out.append(capo_panorama.types.node_from_template_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeFromTemplateJobList:
    import capo_panorama.types.node_from_template_job

    out: NodeFromTemplateJobList = []
    for item in data:
        out.append(capo_panorama.types.node_from_template_job.deserialize_json(item))
    return out
