"""Generated from Smithy shape ``com.amazonaws.mq#DescribeBrokerEngineTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__integer_min5_max100
    import capo_mq.types.__list_of_broker_engine_type
    import capo_mq.types.__string


class DescribeBrokerEngineTypesResponse(TypedDict, closed=True):
    broker_engine_types: NotRequired[
        "capo_mq.types.__list_of_broker_engine_type.__listOfBrokerEngineType"
    ]
    """<p>List of available engine types and versions.</p>"""
    max_results: NotRequired["capo_mq.types.__integer_min5_max100.__integerMin5Max100"]
    """<p>Required. The maximum number of engine types that can be returned per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["capo_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrokerEngineTypesResponse) -> dict:
    out: dict = {}
    if "broker_engine_types" in value:
        import capo_mq.types.__list_of_broker_engine_type

        out["brokerEngineTypes"] = (
            capo_mq.types.__list_of_broker_engine_type.serialize_json(
                value["broker_engine_types"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeBrokerEngineTypesResponse:
    out: DescribeBrokerEngineTypesResponse = {}  # type: ignore[typeddict-item]
    if "brokerEngineTypes" in data:
        import capo_mq.types.__list_of_broker_engine_type

        out["broker_engine_types"] = (
            capo_mq.types.__list_of_broker_engine_type.deserialize_json(
                data["brokerEngineTypes"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
