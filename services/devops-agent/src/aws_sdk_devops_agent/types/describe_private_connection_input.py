"""Generated from Smithy shape ``com.amazonaws.devopsagent#DescribePrivateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_name


class DescribePrivateConnectionInput(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePrivateConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePrivateConnectionInput:
    out: DescribePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    return out
