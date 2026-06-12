"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListCompositionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.encoder_configuration_arn
    import aws_sdk_ivs_realtime.types.max_composition_results
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.stage_arn


class ListCompositionsRequest(TypedDict):
    filter_by_stage_arn: NotRequired["aws_sdk_ivs_realtime.types.stage_arn.StageArn"]
    """<p>Filters the Composition list to match the specified Stage ARN.</p>"""
    filter_by_encoder_configuration_arn: NotRequired[
        "aws_sdk_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    ]
    """<p>Filters the Composition list to match the specified EncoderConfiguration attached to at least one of its output.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first Composition to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_composition_results.MaxCompositionResults"
    ]
    """<p>Maximum number of results to return. Default: 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCompositionsRequest) -> dict:
    out: dict = {}
    if "filter_by_stage_arn" in value:
        out["filterByStageArn"] = value["filter_by_stage_arn"]
    if "filter_by_encoder_configuration_arn" in value:
        out["filterByEncoderConfigurationArn"] = value[
            "filter_by_encoder_configuration_arn"
        ]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListCompositionsRequest:
    out: ListCompositionsRequest = {}  # type: ignore[typeddict-item]
    if "filterByStageArn" in data:
        out["filter_by_stage_arn"] = data["filterByStageArn"]
    if "filterByEncoderConfigurationArn" in data:
        out["filter_by_encoder_configuration_arn"] = data[
            "filterByEncoderConfigurationArn"
        ]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
