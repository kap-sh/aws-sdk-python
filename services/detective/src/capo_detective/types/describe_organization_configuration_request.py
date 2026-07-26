"""Generated from Smithy shape ``com.amazonaws.detective#DescribeOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_detective.errors import DeserializationError

if TYPE_CHECKING:
    import capo_detective.types.graph_arn


class DescribeOrganizationConfigurationRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the organization behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> DescribeOrganizationConfigurationRequest:
    out: DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError(
            "DescribeOrganizationConfigurationRequest.graph_arn required"
        )
    return out
