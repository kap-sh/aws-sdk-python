"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeRegistriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.next_token
    import aws_sdk_ecr_public.types.registry_list


class DescribeRegistriesResponse(TypedDict):
    registries: "aws_sdk_ecr_public.types.registry_list.RegistryList"
    """<p>An object that contains the details for a public registry.</p>"""
    next_token: NotRequired["aws_sdk_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeRepositories</code> request. If the results of a <code>DescribeRepositories</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. If there are no more results, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistriesResponse) -> dict:
    out: dict = {}
    import aws_sdk_ecr_public.types.registry_list

    out["registries"] = aws_sdk_ecr_public.types.registry_list.serialize_aws_json_1_1(
        value["registries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistriesResponse:
    out: DescribeRegistriesResponse = {}  # type: ignore[typeddict-item]
    if "registries" in data:
        import aws_sdk_ecr_public.types.registry_list

        out["registries"] = (
            aws_sdk_ecr_public.types.registry_list.deserialize_aws_json_1_1(
                data["registries"]
            )
        )
    else:
        raise DeserializationError("DescribeRegistriesResponse.registries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
