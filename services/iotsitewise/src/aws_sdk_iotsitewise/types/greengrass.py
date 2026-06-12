"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Greengrass``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn


class Greengrass(TypedDict):
    group_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the Greengrass group. For more information about how to find a group's ARN, see <a href=\"https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html\">ListGroups</a> and <a href=\"https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html\">GetGroup</a> in the <i>IoT Greengrass V1 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Greengrass) -> dict:
    out: dict = {}
    out["groupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> Greengrass:
    out: Greengrass = {}  # type: ignore[typeddict-item]
    if "groupArn" in data:
        out["group_arn"] = data["groupArn"]
    else:
        raise DeserializationError("Greengrass.group_arn required")
    return out
