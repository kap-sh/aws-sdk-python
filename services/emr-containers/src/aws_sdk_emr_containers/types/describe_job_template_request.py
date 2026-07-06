"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DescribeJobTemplateRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the job template that will be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobTemplateRequest:
    out: DescribeJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
