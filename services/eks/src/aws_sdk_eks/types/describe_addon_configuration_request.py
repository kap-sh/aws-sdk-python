"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAddonConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DescribeAddonConfigurationRequest(TypedDict):
    addon_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the add-on. The name must match one of the names returned by <code>DescribeAddonVersions</code>.</p>"""
    addon_version: "aws_sdk_eks.types.string.String"
    """<p>The version of the add-on. The version must match one of the versions returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\"> <code>DescribeAddonVersions</code> </a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAddonConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAddonConfigurationRequest:
    out: DescribeAddonConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
