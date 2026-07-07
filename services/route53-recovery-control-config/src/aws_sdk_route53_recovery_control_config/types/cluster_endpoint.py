"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ClusterEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max32_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max128_pattern_a_za_z09


class ClusterEndpoint(TypedDict, closed=True):
    endpoint: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max128_pattern_a_za_z09.__stringMin1Max128PatternAZaZ09"
    ]
    """<p>A cluster endpoint. Specify an endpoint and Amazon Web Services Region when you want to set or retrieve a routing control state in the cluster.</p> <p>To get or update the routing control state, see the Amazon Route 53 Application Recovery Controller Routing Control Actions.</p>"""
    region: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max32_pattern_s.__stringMin1Max32PatternS"
    ]
    """<p>The Amazon Web Services Region for a cluster endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterEndpoint) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> ClusterEndpoint:
    out: ClusterEndpoint = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
