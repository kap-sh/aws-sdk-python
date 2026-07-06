"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_boost_statistics_document_list
    import aws_sdk_xray.types.sampling_statistics_document_list


class GetSamplingTargetsRequest(TypedDict, closed=True):
    sampling_statistics_documents: "aws_sdk_xray.types.sampling_statistics_document_list.SamplingStatisticsDocumentList"
    """<p>Information about rules that the service is using to sample requests.</p>"""
    sampling_boost_statistics_documents: NotRequired[
        "aws_sdk_xray.types.sampling_boost_statistics_document_list.SamplingBoostStatisticsDocumentList"
    ]
    """<p>Information about rules that the service is using to boost sampling rate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingTargetsRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.sampling_statistics_document_list

    out["SamplingStatisticsDocuments"] = (
        aws_sdk_xray.types.sampling_statistics_document_list.serialize_json(
            value["sampling_statistics_documents"]
        )
    )
    if "sampling_boost_statistics_documents" in value:
        import aws_sdk_xray.types.sampling_boost_statistics_document_list

        out["SamplingBoostStatisticsDocuments"] = (
            aws_sdk_xray.types.sampling_boost_statistics_document_list.serialize_json(
                value["sampling_boost_statistics_documents"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSamplingTargetsRequest:
    out: GetSamplingTargetsRequest = {}  # type: ignore[typeddict-item]
    if "SamplingStatisticsDocuments" in data:
        import aws_sdk_xray.types.sampling_statistics_document_list

        out["sampling_statistics_documents"] = (
            aws_sdk_xray.types.sampling_statistics_document_list.deserialize_json(
                data["SamplingStatisticsDocuments"]
            )
        )
    else:
        raise DeserializationError(
            "GetSamplingTargetsRequest.sampling_statistics_documents required"
        )
    if "SamplingBoostStatisticsDocuments" in data:
        import aws_sdk_xray.types.sampling_boost_statistics_document_list

        out["sampling_boost_statistics_documents"] = (
            aws_sdk_xray.types.sampling_boost_statistics_document_list.deserialize_json(
                data["SamplingBoostStatisticsDocuments"]
            )
        )
    return out
