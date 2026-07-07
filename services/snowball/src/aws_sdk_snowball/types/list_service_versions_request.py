"""Generated from Smithy shape ``com.amazonaws.snowball#ListServiceVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.dependent_service_list
    import aws_sdk_snowball.types.list_limit
    import aws_sdk_snowball.types.service_name
    import aws_sdk_snowball.types.string


class ListServiceVersionsRequest(TypedDict, closed=True):
    service_name: "aws_sdk_snowball.types.service_name.ServiceName"
    """<p>The name of the service for which you're requesting supported versions.</p>"""
    dependent_services: NotRequired[
        "aws_sdk_snowball.types.dependent_service_list.DependentServiceList"
    ]
    """<p>A list of names and versions of dependant services of the requested service.</p>"""
    max_results: NotRequired["aws_sdk_snowball.types.list_limit.ListLimit"]
    """<p>The maximum number of <code>ListServiceVersions</code> objects to return.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for the next list of returned <code>ListServiceVersionsRequest</code> versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceVersionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_snowball.types.service_name

    out["ServiceName"] = aws_sdk_snowball.types.service_name.serialize_aws_json_1_1(
        value["service_name"]
    )
    if "dependent_services" in value:
        import aws_sdk_snowball.types.dependent_service_list

        out["DependentServices"] = (
            aws_sdk_snowball.types.dependent_service_list.serialize_aws_json_1_1(
                value["dependent_services"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceVersionsRequest:
    out: ListServiceVersionsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import aws_sdk_snowball.types.service_name

        out["service_name"] = (
            aws_sdk_snowball.types.service_name.deserialize_aws_json_1_1(
                data["ServiceName"]
            )
        )
    else:
        raise DeserializationError("ListServiceVersionsRequest.service_name required")
    if "DependentServices" in data:
        import aws_sdk_snowball.types.dependent_service_list

        out["dependent_services"] = (
            aws_sdk_snowball.types.dependent_service_list.deserialize_aws_json_1_1(
                data["DependentServices"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
