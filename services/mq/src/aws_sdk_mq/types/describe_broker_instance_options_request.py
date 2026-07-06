"""Generated from Smithy shape ``com.amazonaws.mq#DescribeBrokerInstanceOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.max_results


class DescribeBrokerInstanceOptionsRequest(TypedDict, closed=True):
    engine_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Filter response by engine type.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Filter response by host instance type.</p>"""
    max_results: NotRequired["aws_sdk_mq.types.max_results.MaxResults"]
    """<p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""
    storage_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Filter response by storage type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrokerInstanceOptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBrokerInstanceOptionsRequest:
    out: DescribeBrokerInstanceOptionsRequest = {}  # type: ignore[typeddict-item]
    return out
