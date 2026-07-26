"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerBackendServerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.string_list


class AwsElbLoadBalancerBackendServerDescription(TypedDict, closed=True):
    instance_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port on which the EC2 instance is listening.</p>"""
    policy_names: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The names of the policies that are enabled for the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerBackendServerDescription) -> dict:
    out: dict = {}
    if "instance_port" in value:
        out["InstancePort"] = value["instance_port"]
    if "policy_names" in value:
        import capo_securityhub.types.string_list

        out["PolicyNames"] = capo_securityhub.types.string_list.serialize_json(
            value["policy_names"]
        )
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerBackendServerDescription:
    out: AwsElbLoadBalancerBackendServerDescription = {}  # type: ignore[typeddict-item]
    if "InstancePort" in data:
        out["instance_port"] = data["InstancePort"]
    if "PolicyNames" in data:
        import capo_securityhub.types.string_list

        out["policy_names"] = capo_securityhub.types.string_list.deserialize_json(
            data["PolicyNames"]
        )
    return out
