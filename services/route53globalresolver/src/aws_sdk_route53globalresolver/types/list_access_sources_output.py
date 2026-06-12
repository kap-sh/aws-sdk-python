"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListAccessSourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_sources


class ListAccessSourcesOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    access_sources: "aws_sdk_route53globalresolver.types.access_sources.AccessSources"
    """<p>An array containing information about the access sources, such as the ID, CIDR etc.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessSourcesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.access_sources

    out["accessSources"] = (
        aws_sdk_route53globalresolver.types.access_sources.serialize_json(
            value["access_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAccessSourcesOutput:
    out: ListAccessSourcesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accessSources" in data:
        import aws_sdk_route53globalresolver.types.access_sources

        out["access_sources"] = (
            aws_sdk_route53globalresolver.types.access_sources.deserialize_json(
                data["accessSources"]
            )
        )
    else:
        raise DeserializationError("ListAccessSourcesOutput.access_sources required")
    return out
