"""Generated from Smithy shape ``com.amazonaws.machinelearning#Algorithm``."""

from typing import Literal, TypeAlias, cast

"""<p>The function used to train an <code>MLModel</code>. Training choices supported by Amazon ML include the following:</p> <ul> <li> <p> <code>SGD</code> - Stochastic Gradient Descent.</p> </li> <li> <p> <code>RandomForest</code> - Random forest of decision trees.</p> </li> </ul>"""
Algorithm: TypeAlias = Literal["sgd",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Algorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Algorithm:
    return cast(Algorithm, data)
