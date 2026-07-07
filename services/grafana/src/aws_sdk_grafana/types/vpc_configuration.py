"""Generated from Smithy shape ``com.amazonaws.grafana#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.security_group_ids
    import aws_sdk_grafana.types.subnet_ids


class VpcConfiguration(TypedDict, closed=True):
    security_group_ids: "aws_sdk_grafana.types.security_group_ids.SecurityGroupIds"
    """<p>The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.</p>"""
    subnet_ids: "aws_sdk_grafana.types.subnet_ids.SubnetIds"
    """<p>The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect. Duplicates not allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.security_group_ids

    out["securityGroupIds"] = aws_sdk_grafana.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    import aws_sdk_grafana.types.subnet_ids

    out["subnetIds"] = aws_sdk_grafana.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if "securityGroupIds" in data:
        import aws_sdk_grafana.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_grafana.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.security_group_ids required")
    if "subnetIds" in data:
        import aws_sdk_grafana.types.subnet_ids

        out["subnet_ids"] = aws_sdk_grafana.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("VpcConfiguration.subnet_ids required")
    return out
