"""Generated from Smithy shape ``com.amazonaws.synthetics#GetCanaryRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_name
    import aws_sdk_synthetics.types.max_size100
    import aws_sdk_synthetics.types.run_type
    import aws_sdk_synthetics.types.token
    import aws_sdk_synthetics.types.uuid


class GetCanaryRunsRequest(TypedDict, closed=True):
    name: "aws_sdk_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to see runs for.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>GetCanaryRuns</code> operation to retrieve the next set of results.</p> <note> <p>When auto retry is enabled for the canary, the first subsequent retry is suffixed with *1 indicating its the first retry and the next subsequent try is suffixed with *2.</p> </note>"""
    max_results: NotRequired["aws_sdk_synthetics.types.max_size100.MaxSize100"]
    """<p>Specify this parameter to limit how many runs are returned each time you use the <code>GetCanaryRuns</code> operation. If you omit this parameter, the default of 100 is used.</p>"""
    dry_run_id: NotRequired["aws_sdk_synthetics.types.uuid.UUID"]
    """<p>The DryRunId associated with an existing canary’s dry run. You can use this DryRunId to retrieve information about the dry run.</p>"""
    run_type: NotRequired["aws_sdk_synthetics.types.run_type.RunType"]
    """<ul> <li> <p>When you provide <code>RunType=CANARY_RUN</code> and <code>dryRunId</code>, you will get an exception </p> </li> <li> <p>When a value is not provided for <code>RunType</code>, the default value is <code>CANARY_RUN</code> </p> </li> <li> <p>When <code>CANARY_RUN</code> is provided, all canary runs excluding dry runs are returned</p> </li> <li> <p>When <code>DRY_RUN</code> is provided, all dry runs excluding canary runs are returned</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCanaryRunsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "dry_run_id" in value:
        out["DryRunId"] = value["dry_run_id"]
    if "run_type" in value:
        import aws_sdk_synthetics.types.run_type

        out["RunType"] = aws_sdk_synthetics.types.run_type.serialize_json(
            value["run_type"]
        )
    return out


def deserialize_json(data: dict) -> GetCanaryRunsRequest:
    out: GetCanaryRunsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "DryRunId" in data:
        out["dry_run_id"] = data["DryRunId"]
    if "RunType" in data:
        import aws_sdk_synthetics.types.run_type

        out["run_type"] = aws_sdk_synthetics.types.run_type.deserialize_json(
            data["RunType"]
        )
    return out
