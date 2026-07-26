"""Generated from Smithy shape ``com.amazonaws.glue#DescribeIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integrations_list
    import capo_glue.types.string128


class DescribeIntegrationsResponse(TypedDict, closed=True):
    integrations: NotRequired["capo_glue.types.integrations_list.IntegrationsList"]
    """<p>A list of zero-ETL integrations.</p>"""
    marker: NotRequired["capo_glue.types.string128.String128"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIntegrationsResponse) -> dict:
    out: dict = {}
    if "integrations" in value:
        import capo_glue.types.integrations_list

        out["Integrations"] = capo_glue.types.integrations_list.serialize_aws_json_1_1(
            value["integrations"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIntegrationsResponse:
    out: DescribeIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "Integrations" in data:
        import capo_glue.types.integrations_list

        out["integrations"] = (
            capo_glue.types.integrations_list.deserialize_aws_json_1_1(
                data["Integrations"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
