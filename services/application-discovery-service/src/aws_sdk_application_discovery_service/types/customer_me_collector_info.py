"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CustomerMeCollectorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.integer


class CustomerMeCollectorInfo(TypedDict, closed=True):
    active_me_collectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p> The number of active Migration Evaluator collectors. </p>"""
    healthy_me_collectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p> The number of healthy Migration Evaluator collectors. </p>"""
    deny_listed_me_collectors: (
        "aws_sdk_application_discovery_service.types.integer.Integer"
    )
    """<p> The number of deny-listed Migration Evaluator collectors. </p>"""
    shutdown_me_collectors: (
        "aws_sdk_application_discovery_service.types.integer.Integer"
    )
    """<p> The number of Migration Evaluator collectors with <code>SHUTDOWN</code> status. </p>"""
    unhealthy_me_collectors: (
        "aws_sdk_application_discovery_service.types.integer.Integer"
    )
    """<p> The number of unhealthy Migration Evaluator collectors. </p>"""
    total_me_collectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p> The total number of Migration Evaluator collectors. </p>"""
    unknown_me_collectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p> The number of unknown Migration Evaluator collectors. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerMeCollectorInfo) -> dict:
    out: dict = {}
    out["activeMeCollectors"] = value.get("active_me_collectors", 0)
    out["healthyMeCollectors"] = value.get("healthy_me_collectors", 0)
    out["denyListedMeCollectors"] = value.get("deny_listed_me_collectors", 0)
    out["shutdownMeCollectors"] = value.get("shutdown_me_collectors", 0)
    out["unhealthyMeCollectors"] = value.get("unhealthy_me_collectors", 0)
    out["totalMeCollectors"] = value.get("total_me_collectors", 0)
    out["unknownMeCollectors"] = value.get("unknown_me_collectors", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerMeCollectorInfo:
    out: CustomerMeCollectorInfo = {}  # type: ignore[typeddict-item]
    if "activeMeCollectors" in data:
        out["active_me_collectors"] = data["activeMeCollectors"]
    else:
        out["active_me_collectors"] = 0
    if "healthyMeCollectors" in data:
        out["healthy_me_collectors"] = data["healthyMeCollectors"]
    else:
        out["healthy_me_collectors"] = 0
    if "denyListedMeCollectors" in data:
        out["deny_listed_me_collectors"] = data["denyListedMeCollectors"]
    else:
        out["deny_listed_me_collectors"] = 0
    if "shutdownMeCollectors" in data:
        out["shutdown_me_collectors"] = data["shutdownMeCollectors"]
    else:
        out["shutdown_me_collectors"] = 0
    if "unhealthyMeCollectors" in data:
        out["unhealthy_me_collectors"] = data["unhealthyMeCollectors"]
    else:
        out["unhealthy_me_collectors"] = 0
    if "totalMeCollectors" in data:
        out["total_me_collectors"] = data["totalMeCollectors"]
    else:
        out["total_me_collectors"] = 0
    if "unknownMeCollectors" in data:
        out["unknown_me_collectors"] = data["unknownMeCollectors"]
    else:
        out["unknown_me_collectors"] = 0
    return out
