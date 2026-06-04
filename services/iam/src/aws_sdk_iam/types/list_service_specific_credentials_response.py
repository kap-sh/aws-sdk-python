"""Generated from Smithy shape ``com.amazonaws.iam#ListServiceSpecificCredentialsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.boolean_type
    import aws_sdk_iam.types.response_marker_type
    import aws_sdk_iam.types.service_specific_credentials_list_type


class ListServiceSpecificCredentialsResponse(TypedDict):
    service_specific_credentials: NotRequired[
        "aws_sdk_iam.types.service_specific_credentials_list_type.ServiceSpecificCredentialsListType"
    ]
    """<p>A list of structures that each contain details about a service-specific credential.</p>"""
    marker: NotRequired["aws_sdk_iam.types.response_marker_type.responseMarkerType"]
    """<p>When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.</p>"""
    is_truncated: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListServiceSpecificCredentialsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_specific_credentials" in value:
        import aws_sdk_iam.types.service_specific_credentials_list_type

        aws_sdk_iam.types.service_specific_credentials_list_type.serialize_query(
            value["service_specific_credentials"],
            pairs,
            f"{prefix}.ServiceSpecificCredentials",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    pairs.append(
        (
            f"{prefix}.IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )


def deserialize_query(el: Element) -> ListServiceSpecificCredentialsResponse:
    out: ListServiceSpecificCredentialsResponse = {}  # type: ignore[typeddict-item]
    child_service_specific_credentials = el.find("ServiceSpecificCredentials")
    if child_service_specific_credentials is not None:
        import aws_sdk_iam.types.service_specific_credentials_list_type

        out["service_specific_credentials"] = (
            aws_sdk_iam.types.service_specific_credentials_list_type.deserialize_query(
                child_service_specific_credentials
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    return out
