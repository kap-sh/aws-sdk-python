"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.aws_account_id
    import aws_sdk_networkmanager.types.boolean
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.route_analysis_endpoint_options
    import aws_sdk_networkmanager.types.route_analysis_path
    import aws_sdk_networkmanager.types.route_analysis_status


class RouteAnalysis(TypedDict, closed=True):
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_networkmanager.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the AWS account that created the route analysis.</p>"""
    route_analysis_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the route analysis.</p>"""
    start_timestamp: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The time that the analysis started.</p>"""
    status: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis_status.RouteAnalysisStatus"
    ]
    """<p>The status of the route analysis.</p>"""
    source: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis_endpoint_options.RouteAnalysisEndpointOptions"
    ]
    """<p>The source.</p>"""
    destination: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis_endpoint_options.RouteAnalysisEndpointOptions"
    ]
    """<p>The destination.</p>"""
    include_return_path: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether to analyze the return path. The return path is not analyzed if the forward path analysis does not succeed.</p>"""
    use_middleboxes: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether to include the location of middlebox appliances in the route analysis.</p>"""
    forward_path: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis_path.RouteAnalysisPath"
    ]
    """<p>The forward path.</p>"""
    return_path: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis_path.RouteAnalysisPath"
    ]
    """<p>The return path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysis) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "route_analysis_id" in value:
        out["RouteAnalysisId"] = value["route_analysis_id"]
    if "start_timestamp" in value:
        import aws_sdk_networkmanager.types.date_time

        out["StartTimestamp"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["start_timestamp"]
        )
    if "status" in value:
        import aws_sdk_networkmanager.types.route_analysis_status

        out["Status"] = (
            aws_sdk_networkmanager.types.route_analysis_status.serialize_json(
                value["status"]
            )
        )
    if "source" in value:
        import aws_sdk_networkmanager.types.route_analysis_endpoint_options

        out["Source"] = (
            aws_sdk_networkmanager.types.route_analysis_endpoint_options.serialize_json(
                value["source"]
            )
        )
    if "destination" in value:
        import aws_sdk_networkmanager.types.route_analysis_endpoint_options

        out["Destination"] = (
            aws_sdk_networkmanager.types.route_analysis_endpoint_options.serialize_json(
                value["destination"]
            )
        )
    out["IncludeReturnPath"] = value.get("include_return_path", False)
    out["UseMiddleboxes"] = value.get("use_middleboxes", False)
    if "forward_path" in value:
        import aws_sdk_networkmanager.types.route_analysis_path

        out["ForwardPath"] = (
            aws_sdk_networkmanager.types.route_analysis_path.serialize_json(
                value["forward_path"]
            )
        )
    if "return_path" in value:
        import aws_sdk_networkmanager.types.route_analysis_path

        out["ReturnPath"] = (
            aws_sdk_networkmanager.types.route_analysis_path.serialize_json(
                value["return_path"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAnalysis:
    out: RouteAnalysis = {}  # type: ignore[typeddict-item]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "RouteAnalysisId" in data:
        out["route_analysis_id"] = data["RouteAnalysisId"]
    if "StartTimestamp" in data:
        import aws_sdk_networkmanager.types.date_time

        out["start_timestamp"] = (
            aws_sdk_networkmanager.types.date_time.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "Status" in data:
        import aws_sdk_networkmanager.types.route_analysis_status

        out["status"] = (
            aws_sdk_networkmanager.types.route_analysis_status.deserialize_json(
                data["Status"]
            )
        )
    if "Source" in data:
        import aws_sdk_networkmanager.types.route_analysis_endpoint_options

        out["source"] = (
            aws_sdk_networkmanager.types.route_analysis_endpoint_options.deserialize_json(
                data["Source"]
            )
        )
    if "Destination" in data:
        import aws_sdk_networkmanager.types.route_analysis_endpoint_options

        out["destination"] = (
            aws_sdk_networkmanager.types.route_analysis_endpoint_options.deserialize_json(
                data["Destination"]
            )
        )
    if "IncludeReturnPath" in data:
        out["include_return_path"] = data["IncludeReturnPath"]
    else:
        out["include_return_path"] = False
    if "UseMiddleboxes" in data:
        out["use_middleboxes"] = data["UseMiddleboxes"]
    else:
        out["use_middleboxes"] = False
    if "ForwardPath" in data:
        import aws_sdk_networkmanager.types.route_analysis_path

        out["forward_path"] = (
            aws_sdk_networkmanager.types.route_analysis_path.deserialize_json(
                data["ForwardPath"]
            )
        )
    if "ReturnPath" in data:
        import aws_sdk_networkmanager.types.route_analysis_path

        out["return_path"] = (
            aws_sdk_networkmanager.types.route_analysis_path.deserialize_json(
                data["ReturnPath"]
            )
        )
    return out
