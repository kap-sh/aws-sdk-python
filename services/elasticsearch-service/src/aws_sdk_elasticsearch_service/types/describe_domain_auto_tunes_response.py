"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeDomainAutoTunesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.auto_tune_list
    import aws_sdk_elasticsearch_service.types.next_token


class DescribeDomainAutoTunesResponse(TypedDict):
    auto_tunes: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_list.AutoTuneList"
    ]
    """<p>Specifies the list of setting adjustments that Auto-Tune has made to the domain. See the <a href=\"https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html\" target=\"_blank\">Developer Guide</a> for more information.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Specifies an identifier to allow retrieval of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainAutoTunesResponse) -> dict:
    out: dict = {}
    if "auto_tunes" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_list

        out["AutoTunes"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_list.serialize_json(
                value["auto_tunes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeDomainAutoTunesResponse:
    out: DescribeDomainAutoTunesResponse = {}  # type: ignore[typeddict-item]
    if "AutoTunes" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_list

        out["auto_tunes"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_list.deserialize_json(
                data["AutoTunes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
