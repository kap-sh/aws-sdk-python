"""Generated from Smithy shape ``com.amazonaws.emr#ListSupportedInstanceTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.supported_instance_types_list


class ListSupportedInstanceTypesOutput(TypedDict, closed=True):
    supported_instance_types: NotRequired[
        "aws_sdk_emr.types.supported_instance_types_list.SupportedInstanceTypesList"
    ]
    """<p>The list of instance types that the release specified in <code>ListSupportedInstanceTypesInput$ReleaseLabel</code> supports, filtered by Amazon Web Services Region.</p>"""
    marker: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The pagination token that marks the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSupportedInstanceTypesOutput) -> dict:
    out: dict = {}
    if "supported_instance_types" in value:
        import aws_sdk_emr.types.supported_instance_types_list

        out["SupportedInstanceTypes"] = (
            aws_sdk_emr.types.supported_instance_types_list.serialize_aws_json_1_1(
                value["supported_instance_types"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSupportedInstanceTypesOutput:
    out: ListSupportedInstanceTypesOutput = {}  # type: ignore[typeddict-item]
    if "SupportedInstanceTypes" in data:
        import aws_sdk_emr.types.supported_instance_types_list

        out["supported_instance_types"] = (
            aws_sdk_emr.types.supported_instance_types_list.deserialize_aws_json_1_1(
                data["SupportedInstanceTypes"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
