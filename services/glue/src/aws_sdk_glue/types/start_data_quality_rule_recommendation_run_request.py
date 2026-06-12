"""Generated from Smithy shape ``com.amazonaws.glue#StartDataQualityRuleRecommendationRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.role_string
    import aws_sdk_glue.types.timeout


class StartDataQualityRuleRecommendationRunRequest(TypedDict):
    data_source: "aws_sdk_glue.types.data_source.DataSource"
    """<p>The data source (Glue table) associated with this run.</p>"""
    role: "aws_sdk_glue.types.role_string.RoleString"
    """<p>An IAM role supplied to encrypt the results of the run.</p>"""
    number_of_workers: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["aws_sdk_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    created_ruleset_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>A name for the ruleset.</p>"""
    data_quality_security_configuration: NotRequired[
        "aws_sdk_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""
    client_token: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataQualityRuleRecommendationRunRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.data_source

    out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    out["Role"] = value["role"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "created_ruleset_name" in value:
        out["CreatedRulesetName"] = value["created_ruleset_name"]
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartDataQualityRuleRecommendationRunRequest:
    out: StartDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    else:
        raise DeserializationError(
            "StartDataQualityRuleRecommendationRunRequest.data_source required"
        )
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError(
            "StartDataQualityRuleRecommendationRunRequest.role required"
        )
    if "NumberOfWorkers" in data:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "CreatedRulesetName" in data:
        out["created_ruleset_name"] = data["CreatedRulesetName"]
    if "DataQualitySecurityConfiguration" in data:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
