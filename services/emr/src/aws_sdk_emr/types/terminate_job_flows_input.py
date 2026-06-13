"""Generated from Smithy shape ``com.amazonaws.emr#TerminateJobFlowsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_list


class TerminateJobFlowsInput(TypedDict):
    job_flow_ids: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>A list of job flows to be shut down.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateJobFlowsInput) -> dict:
    out: dict = {}
    if "job_flow_ids" in value:
        import aws_sdk_emr.types.xml_string_list

        out["JobFlowIds"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateJobFlowsInput:
    out: TerminateJobFlowsInput = {}  # type: ignore[typeddict-item]
    if "JobFlowIds" in data:
        import aws_sdk_emr.types.xml_string_list

        out["job_flow_ids"] = (
            aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
                data["JobFlowIds"]
            )
        )
    return out
