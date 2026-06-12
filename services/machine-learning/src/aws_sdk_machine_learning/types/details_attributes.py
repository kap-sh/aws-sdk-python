"""Generated from Smithy shape ``com.amazonaws.machinelearning#DetailsAttributes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

"""<p>Contains the key values of <code>DetailsMap</code>:</p> <ul> <li> <p> <code>PredictiveModelType</code> - Indicates the type of the <code>MLModel</code>.</p> </li> <li> <p> <code>Algorithm</code> - Indicates the algorithm that was used for the <code>MLModel</code>.</p> </li> </ul>"""
DetailsAttributes: TypeAlias = Literal[
    "PredictiveModelType",
    "Algorithm",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PredictiveModelType",
        "Algorithm",
    )
)


def serialize_aws_json_1_1(value: DetailsAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailsAttributes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailsAttributes value: {data!r}")
    return cast(DetailsAttributes, data)
