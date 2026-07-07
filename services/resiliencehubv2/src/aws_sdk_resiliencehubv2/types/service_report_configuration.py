"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.report_output_configuration_list


class ServiceReportConfiguration(TypedDict, closed=True):
    report_outputs: "aws_sdk_resiliencehubv2.types.report_output_configuration_list.ReportOutputConfigurationList"
    """<p>Output destinations for generated reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReportConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.report_output_configuration_list

    out["reportOutputs"] = (
        aws_sdk_resiliencehubv2.types.report_output_configuration_list.serialize_json(
            value["report_outputs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceReportConfiguration:
    out: ServiceReportConfiguration = {}  # type: ignore[typeddict-item]
    if "reportOutputs" in data:
        import aws_sdk_resiliencehubv2.types.report_output_configuration_list

        out["report_outputs"] = (
            aws_sdk_resiliencehubv2.types.report_output_configuration_list.deserialize_json(
                data["reportOutputs"]
            )
        )
    else:
        raise DeserializationError("ServiceReportConfiguration.report_outputs required")
    return out
