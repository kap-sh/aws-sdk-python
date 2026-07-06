"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerListenerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_listener
    import aws_sdk_securityhub.types.string_list


class AwsElbLoadBalancerListenerDescription(TypedDict, closed=True):
    listener: NotRequired[
        "aws_sdk_securityhub.types.aws_elb_load_balancer_listener.AwsElbLoadBalancerListener"
    ]
    """<p>Information about the listener.</p>"""
    policy_names: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The policies enabled for the listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerListenerDescription) -> dict:
    out: dict = {}
    if "listener" in value:
        import aws_sdk_securityhub.types.aws_elb_load_balancer_listener

        out["Listener"] = (
            aws_sdk_securityhub.types.aws_elb_load_balancer_listener.serialize_json(
                value["listener"]
            )
        )
    if "policy_names" in value:
        import aws_sdk_securityhub.types.string_list

        out["PolicyNames"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["policy_names"]
        )
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerListenerDescription:
    out: AwsElbLoadBalancerListenerDescription = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import aws_sdk_securityhub.types.aws_elb_load_balancer_listener

        out["listener"] = (
            aws_sdk_securityhub.types.aws_elb_load_balancer_listener.deserialize_json(
                data["Listener"]
            )
        )
    if "PolicyNames" in data:
        import aws_sdk_securityhub.types.string_list

        out["policy_names"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["PolicyNames"]
        )
    return out
