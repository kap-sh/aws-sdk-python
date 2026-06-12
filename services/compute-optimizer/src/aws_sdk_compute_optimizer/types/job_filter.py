"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.filter_values
    import aws_sdk_compute_optimizer.types.job_filter_name


class JobFilter(TypedDict):
    name: NotRequired["aws_sdk_compute_optimizer.types.job_filter_name.JobFilterName"]
    """<p>The name of the filter.</p> <p>Specify <code>ResourceType</code> to return export jobs of a specific resource type (for example, <code>Ec2Instance</code>).</p> <p>Specify <code>JobStatus</code> to return export jobs with a specific status (e.g, <code>Complete</code>).</p>"""
    values: NotRequired["aws_sdk_compute_optimizer.types.filter_values.FilterValues"]
    """<p>The value of the filter.</p> <p>The valid values for this parameter are as follows, depending on what you specify for the <code>name</code> parameter:</p> <ul> <li> <p>Specify <code>Ec2Instance</code> or <code>AutoScalingGroup</code> if you specify the <code>name</code> parameter as <code>ResourceType</code>. There is no filter for EBS volumes because volume recommendations cannot be exported at this time.</p> </li> <li> <p>Specify <code>Queued</code>, <code>InProgress</code>, <code>Complete</code>, or <code>Failed</code> if you specify the <code>name</code> parameter as <code>JobStatus</code>.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.job_filter_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.job_filter_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_compute_optimizer.types.filter_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.filter_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> JobFilter:
    out: JobFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.job_filter_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.job_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_compute_optimizer.types.filter_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
