"""Generated from Smithy shape ``com.amazonaws.mq#DescribeBrokerInstanceOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer_min5_max100
    import aws_sdk_mq.types.__list_of_broker_instance_option
    import aws_sdk_mq.types.__string


class DescribeBrokerInstanceOptionsResponse(TypedDict, closed=True):
    broker_instance_options: NotRequired[
        "aws_sdk_mq.types.__list_of_broker_instance_option.__listOfBrokerInstanceOption"
    ]
    """<p>List of available broker instance options.</p>"""
    max_results: NotRequired[
        "aws_sdk_mq.types.__integer_min5_max100.__integerMin5Max100"
    ]
    """<p>Required. The maximum number of instance options that can be returned per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrokerInstanceOptionsResponse) -> dict:
    out: dict = {}
    if "broker_instance_options" in value:
        import aws_sdk_mq.types.__list_of_broker_instance_option

        out["brokerInstanceOptions"] = (
            aws_sdk_mq.types.__list_of_broker_instance_option.serialize_json(
                value["broker_instance_options"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeBrokerInstanceOptionsResponse:
    out: DescribeBrokerInstanceOptionsResponse = {}  # type: ignore[typeddict-item]
    if "brokerInstanceOptions" in data:
        import aws_sdk_mq.types.__list_of_broker_instance_option

        out["broker_instance_options"] = (
            aws_sdk_mq.types.__list_of_broker_instance_option.deserialize_json(
                data["brokerInstanceOptions"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
