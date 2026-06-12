"""Generated from Smithy shape ``com.amazonaws.snowball#ListServiceVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.dependent_service_list
    import aws_sdk_snowball.types.service_name
    import aws_sdk_snowball.types.service_version_list
    import aws_sdk_snowball.types.string


class ListServiceVersionsResult(TypedDict):
    service_versions: "aws_sdk_snowball.types.service_version_list.ServiceVersionList"
    """<p>A list of supported versions.</p>"""
    service_name: "aws_sdk_snowball.types.service_name.ServiceName"
    """<p>The name of the service for which the system provided supported versions.</p>"""
    dependent_services: NotRequired[
        "aws_sdk_snowball.types.dependent_service_list.DependentServiceList"
    ]
    """<p>A list of names and versions of dependant services of the service for which the system provided supported versions.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point of the next list of returned <code>ListServiceVersionsResult</code> results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceVersionsResult) -> dict:
    out: dict = {}
    import aws_sdk_snowball.types.service_version_list

    out["ServiceVersions"] = (
        aws_sdk_snowball.types.service_version_list.serialize_aws_json_1_1(
            value["service_versions"]
        )
    )
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
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceVersionsResult:
    out: ListServiceVersionsResult = {}  # type: ignore[typeddict-item]
    if "ServiceVersions" in data:
        import aws_sdk_snowball.types.service_version_list

        out["service_versions"] = (
            aws_sdk_snowball.types.service_version_list.deserialize_aws_json_1_1(
                data["ServiceVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceVersionsResult.service_versions required"
        )
    if "ServiceName" in data:
        import aws_sdk_snowball.types.service_name

        out["service_name"] = (
            aws_sdk_snowball.types.service_name.deserialize_aws_json_1_1(
                data["ServiceName"]
            )
        )
    else:
        raise DeserializationError("ListServiceVersionsResult.service_name required")
    if "DependentServices" in data:
        import aws_sdk_snowball.types.dependent_service_list

        out["dependent_services"] = (
            aws_sdk_snowball.types.dependent_service_list.deserialize_aws_json_1_1(
                data["DependentServices"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
