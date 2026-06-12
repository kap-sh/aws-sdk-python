"""Generated from Smithy shape ``com.amazonaws.iot#BatchConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.batch_across_topics
    import aws_sdk_iot.types.max_batch_open_ms
    import aws_sdk_iot.types.max_batch_size
    import aws_sdk_iot.types.max_batch_size_bytes


class BatchConfig(TypedDict):
    max_batch_open_ms: NotRequired["aws_sdk_iot.types.max_batch_open_ms.MaxBatchOpenMs"]
    """<p>The maximum amount of time (in milliseconds) that an outgoing call waits for other calls with which it batches messages of the same type. The higher the setting, the longer the latency of the batched HTTP Action will be.</p>"""
    max_batch_size: NotRequired["aws_sdk_iot.types.max_batch_size.MaxBatchSize"]
    """<p>The maximum number of messages that are batched together in a single action execution.</p>"""
    max_batch_size_bytes: NotRequired[
        "aws_sdk_iot.types.max_batch_size_bytes.MaxBatchSizeBytes"
    ]
    """<p>Maximum size of a message batch, in bytes.</p>"""
    batch_across_topics: "aws_sdk_iot.types.batch_across_topics.BatchAcrossTopics"
    """<p>Whether to allow batching messages from different MQTT topics into a single HTTP request. By default, only messages from the same topic are batched together. The default value is <code>false</code>.</p> <note> <p>When <code>batchAcrossTopics</code> is enabled, the error payload format changes: the <code>topic</code> field moves from the top level to inside each entry in the <code>payloadsWithMetadata</code> array, since each message in the batch may originate from a different topic.</p> </note> <note> <p>Messages are always batched within the scope of the same account, rule name, target HTTP endpoint URL, and billing group. Messages that differ in any of these attributes are never combined into the same batch, regardless of the <code>batchAcrossTopics</code> setting.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchConfig) -> dict:
    out: dict = {}
    if "max_batch_open_ms" in value:
        out["maxBatchOpenMs"] = value["max_batch_open_ms"]
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "max_batch_size_bytes" in value:
        out["maxBatchSizeBytes"] = value["max_batch_size_bytes"]
    out["batchAcrossTopics"] = value.get("batch_across_topics", False)
    return out


def deserialize_json(data: dict) -> BatchConfig:
    out: BatchConfig = {}  # type: ignore[typeddict-item]
    if "maxBatchOpenMs" in data:
        out["max_batch_open_ms"] = data["maxBatchOpenMs"]
    if "maxBatchSize" in data:
        out["max_batch_size"] = data["maxBatchSize"]
    if "maxBatchSizeBytes" in data:
        out["max_batch_size_bytes"] = data["maxBatchSizeBytes"]
    if "batchAcrossTopics" in data:
        out["batch_across_topics"] = data["batchAcrossTopics"]
    else:
        out["batch_across_topics"] = False
    return out
