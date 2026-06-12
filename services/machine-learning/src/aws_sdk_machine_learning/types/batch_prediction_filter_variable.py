"""Generated from Smithy shape ``com.amazonaws.machinelearning#BatchPredictionFilterVariable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

"""<p>A list of the variables to use in searching or filtering <code>BatchPrediction</code>.</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to <code>BatchPrediction</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to <code>BatchPrediction</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>BatchPrediction</code> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked the <code>BatchPrediction</code> creation.</p> </li> <li> <p> <code>MLModelId</code> - Sets the search criteria to the <code>MLModel</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used in the <code>BatchPrediction</code>.</p> </li> <li> <p> <code>DataURI</code> - Sets the search criteria to the data file(s) used in the <code>BatchPrediction</code>. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.</p> </li> </ul>"""
BatchPredictionFilterVariable: TypeAlias = Literal[
    "CreatedAt",
    "LastUpdatedAt",
    "Status",
    "Name",
    "IAMUser",
    "MLModelId",
    "DataSourceId",
    "DataURI",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreatedAt",
        "LastUpdatedAt",
        "Status",
        "Name",
        "IAMUser",
        "MLModelId",
        "DataSourceId",
        "DataURI",
    )
)


def serialize_aws_json_1_1(value: BatchPredictionFilterVariable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchPredictionFilterVariable:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchPredictionFilterVariable value: {data!r}"
        )
    return cast(BatchPredictionFilterVariable, data)
