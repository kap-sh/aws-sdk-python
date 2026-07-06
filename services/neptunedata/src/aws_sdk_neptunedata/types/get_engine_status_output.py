"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetEngineStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.document_valued_map
    import aws_sdk_neptunedata.types.query_language_version
    import aws_sdk_neptunedata.types.string_valued_map


class GetEngineStatusOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>Set to <code>healthy</code> if the instance is not experiencing problems. If the instance is recovering from a crash or from being rebooted and there are active transactions running from the latest server shutdown, status is set to <code>recovery</code>.</p>"""
    start_time: NotRequired["str"]
    """<p>Set to the UTC time at which the current server process started.</p>"""
    db_engine_version: NotRequired["str"]
    """<p>Set to the Neptune engine version running on your DB cluster. If this engine version has been manually patched since it was released, the version number is prefixed by <code>Patch-</code>.</p>"""
    role: NotRequired["str"]
    """<p>Set to <code>reader</code> if the instance is a read-replica, or to <code>writer</code> if the instance is the primary instance.</p>"""
    dfe_query_engine: NotRequired["str"]
    """<p>Set to <code>enabled</code> if the DFE engine is fully enabled, or to <code>viaQueryHint</code> (the default) if the DFE engine is only used with queries that have the <code>useDFE</code> query hint set to <code>true</code>.</p>"""
    gremlin: NotRequired[
        "aws_sdk_neptunedata.types.query_language_version.QueryLanguageVersion"
    ]
    """<p>Contains information about the Gremlin query language available on your cluster. Specifically, it contains a version field that specifies the current TinkerPop version being used by the engine.</p>"""
    sparql: NotRequired[
        "aws_sdk_neptunedata.types.query_language_version.QueryLanguageVersion"
    ]
    """<p>Contains information about the SPARQL query language available on your cluster. Specifically, it contains a version field that specifies the current SPARQL version being used by the engine.</p>"""
    opencypher: NotRequired[
        "aws_sdk_neptunedata.types.query_language_version.QueryLanguageVersion"
    ]
    """<p>Contains information about the openCypher query language available on your cluster. Specifically, it contains a version field that specifies the current operCypher version being used by the engine.</p>"""
    lab_mode: NotRequired["aws_sdk_neptunedata.types.string_valued_map.StringValuedMap"]
    """<p>Contains Lab Mode settings being used by the engine.</p>"""
    rolling_back_trx_count: NotRequired["int"]
    """<p>If there are transactions being rolled back, this field is set to the number of such transactions. If there are none, the field doesn't appear at all.</p>"""
    rolling_back_trx_earliest_start_time: NotRequired["str"]
    """<p>Set to the start time of the earliest transaction being rolled back. If no transactions are being rolled back, the field doesn't appear at all.</p>"""
    features: NotRequired[
        "aws_sdk_neptunedata.types.document_valued_map.DocumentValuedMap"
    ]
    """<p>Contains status information about the features enabled on your DB cluster.</p>"""
    settings: NotRequired["aws_sdk_neptunedata.types.string_valued_map.StringValuedMap"]
    """<p>Contains information about the current settings on your DB cluster. For example, contains the current cluster query timeout setting (<code>clusterQueryTimeoutInMs</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEngineStatusOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "db_engine_version" in value:
        out["dbEngineVersion"] = value["db_engine_version"]
    if "role" in value:
        out["role"] = value["role"]
    if "dfe_query_engine" in value:
        out["dfeQueryEngine"] = value["dfe_query_engine"]
    if "gremlin" in value:
        import aws_sdk_neptunedata.types.query_language_version

        out["gremlin"] = (
            aws_sdk_neptunedata.types.query_language_version.serialize_json(
                value["gremlin"]
            )
        )
    if "sparql" in value:
        import aws_sdk_neptunedata.types.query_language_version

        out["sparql"] = aws_sdk_neptunedata.types.query_language_version.serialize_json(
            value["sparql"]
        )
    if "opencypher" in value:
        import aws_sdk_neptunedata.types.query_language_version

        out["opencypher"] = (
            aws_sdk_neptunedata.types.query_language_version.serialize_json(
                value["opencypher"]
            )
        )
    if "lab_mode" in value:
        import aws_sdk_neptunedata.types.string_valued_map

        out["labMode"] = aws_sdk_neptunedata.types.string_valued_map.serialize_json(
            value["lab_mode"]
        )
    if "rolling_back_trx_count" in value:
        out["rollingBackTrxCount"] = value["rolling_back_trx_count"]
    if "rolling_back_trx_earliest_start_time" in value:
        out["rollingBackTrxEarliestStartTime"] = value[
            "rolling_back_trx_earliest_start_time"
        ]
    if "features" in value:
        import aws_sdk_neptunedata.types.document_valued_map

        out["features"] = aws_sdk_neptunedata.types.document_valued_map.serialize_json(
            value["features"]
        )
    if "settings" in value:
        import aws_sdk_neptunedata.types.string_valued_map

        out["settings"] = aws_sdk_neptunedata.types.string_valued_map.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> GetEngineStatusOutput:
    out: GetEngineStatusOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "dbEngineVersion" in data:
        out["db_engine_version"] = data["dbEngineVersion"]
    if "role" in data:
        out["role"] = data["role"]
    if "dfeQueryEngine" in data:
        out["dfe_query_engine"] = data["dfeQueryEngine"]
    if "gremlin" in data:
        import aws_sdk_neptunedata.types.query_language_version

        out["gremlin"] = (
            aws_sdk_neptunedata.types.query_language_version.deserialize_json(
                data["gremlin"]
            )
        )
    if "sparql" in data:
        import aws_sdk_neptunedata.types.query_language_version

        out["sparql"] = (
            aws_sdk_neptunedata.types.query_language_version.deserialize_json(
                data["sparql"]
            )
        )
    if "opencypher" in data:
        import aws_sdk_neptunedata.types.query_language_version

        out["opencypher"] = (
            aws_sdk_neptunedata.types.query_language_version.deserialize_json(
                data["opencypher"]
            )
        )
    if "labMode" in data:
        import aws_sdk_neptunedata.types.string_valued_map

        out["lab_mode"] = aws_sdk_neptunedata.types.string_valued_map.deserialize_json(
            data["labMode"]
        )
    if "rollingBackTrxCount" in data:
        out["rolling_back_trx_count"] = data["rollingBackTrxCount"]
    if "rollingBackTrxEarliestStartTime" in data:
        out["rolling_back_trx_earliest_start_time"] = data[
            "rollingBackTrxEarliestStartTime"
        ]
    if "features" in data:
        import aws_sdk_neptunedata.types.document_valued_map

        out["features"] = (
            aws_sdk_neptunedata.types.document_valued_map.deserialize_json(
                data["features"]
            )
        )
    if "settings" in data:
        import aws_sdk_neptunedata.types.string_valued_map

        out["settings"] = aws_sdk_neptunedata.types.string_valued_map.deserialize_json(
            data["settings"]
        )
    return out
