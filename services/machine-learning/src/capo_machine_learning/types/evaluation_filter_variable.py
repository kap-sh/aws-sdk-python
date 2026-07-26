"""Generated from Smithy shape ``com.amazonaws.machinelearning#EvaluationFilterVariable``."""

from typing import Literal, TypeAlias, cast

"""<p>A list of the variables to use in searching or filtering <code>Evaluation</code>.</p> <ul> <li> <p> <code>CreatedAt</code> - Sets the search criteria to <code>Evaluation</code> creation date.</p> </li> <li> <p> <code>Status</code> - Sets the search criteria to <code>Evaluation</code> status.</p> </li> <li> <p> <code>Name</code> - Sets the search criteria to the contents of <code>Evaluation</code> <b> </b> <code>Name</code>.</p> </li> <li> <p> <code>IAMUser</code> - Sets the search criteria to the user account that invoked an evaluation.</p> </li> <li> <p> <code>MLModelId</code> - Sets the search criteria to the <code>Predictor</code> that was evaluated.</p> </li> <li> <p> <code>DataSourceId</code> - Sets the search criteria to the <code>DataSource</code> used in evaluation.</p> </li> <li> <p> <code>DataUri</code> - Sets the search criteria to the data file(s) used in evaluation. The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.</p> </li> </ul>"""
EvaluationFilterVariable: TypeAlias = Literal[
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
def serialize_aws_json_1_1(value: EvaluationFilterVariable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationFilterVariable:
    return cast(EvaluationFilterVariable, data)
